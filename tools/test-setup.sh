#!/bin/bash
#
# This tool is used to setup the environment for running the tests. Its name
# name and location is based on Zuul CI, which can automatically run it.
# (cspell: disable-next-line)
set -euo pipefail

PIP_LOG_FILE=out/log/pip.log
HOSTNAME="${HOSTNAME:-localhost}"
ERR=0
NC='\033[0m' # No Color

mkdir -p out/log
# we do not want pip logs from previous runs
:> "${PIP_LOG_FILE}"

# Function to retrieve the version number for a specific command. If a second
# argument is passed, it will be used as return value when tool is missing.
get_version () {
    if command -v "${1:-}" >/dev/null 2>&1; then
        _cmd=("${@:1}")
        # if we did not pass any arguments, we add --version ourselves:
        if [[ $# -eq 1 ]]; then
            _cmd+=('--version')
        fi
        "${_cmd[@]}" | head -n1 | sed -r 's/^[^0-9]*([0-9][0-9\\w\\.]*).*$/\1/'
    else
        log error "Got $? while trying to retrieve ${1:-} version"
        return 99
    fi
}

# Use "log [notice|warning|error] message" to  print a colored message to
# stderr, with colors.
log () {
    local prefix
    if [ "$#" -ne 2 ]; then
        log error "Incorrect call ($*), use: log [notice|warning|error] 'message'."
        exit 2
    fi
    case $1 in
        notice)   prefix='\033[0;36mNOTICE:  ';;
        warning)  prefix='\033[0;33mWARNING: ';;
        error)    prefix='\033[0;31mERROR:   ';;
        *)        log error "log first argument must be 'notice', 'warning' or 'error', not $1."; exit 2;;
    esac
    >&2 echo -e "${prefix}${2}${NC}"
}

# User specific environment
if ! [[ "${PATH}" == *"${HOME}/.local/bin"* ]]; then
    # shellcheck disable=SC2088
    log warning "~/.local/bin was not found in PATH, attempting to add it."
    cat >>"${HOME}/.bashrc" <<EOF
# User specific environment
if ! [[ "${PATH}" =~ "${HOME}/.local/bin" ]]; then
    PATH="${HOME}/.local/bin:${PATH}"
fi
export PATH
EOF
    PATH="${HOME}/.local/bin:${PATH}"
fi
# install gh if missing
command -v gh >/dev/null 2>&1 || {
    log notice "Trying to install missing gh on ${OS:-null} ..."
    # https://github.com/cli/cli/blob/trunk/docs/install_linux.md
    if [[ -f "/usr/bin/apt-get" ]]; then
      curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | \
          sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
      sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg
      echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
      sudo apt update
      sudo apt install gh
    else
        command -v dnf >/dev/null 2>&1 && sudo dnf install -y gh
    fi
    gh --version || log warning "gh cli not found and it might be needed for some commands."
}
VIRTUAL_ENV=${VIRTUAL_ENV:-out/venvs/${HOSTNAME}}
if [[ ! -d "${VIRTUAL_ENV}" ]]; then
    log notice "Creating virtualenv ..."
    python3 -m venv "${VIRTUAL_ENV}"
fi
# shellcheck disable=SC1091
. "${VIRTUAL_ENV}/bin/activate"

python3 -m pip install -q -U pip

if [[ $(uname || true) != MINGW* ]]; then # if we are not on pure Windows
    python3 -m pip install -q \
        -c .config/requirements.txt -r .config/requirements.in
fi


command -v nvm >/dev/null 2>&1 || {
    # define its location (needed)
    [[ -z "${NVM_DIR:-}" ]] && export NVM_DIR="${HOME}/.nvm";
    # install if missing
    [[ ! -s "${NVM_DIR:-}/nvm.sh" ]] && {
        log warning "Installing missing nvm"
        curl -s -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
    }
    # activate nvm
    # shellcheck disable=1091
    . "${NVM_DIR:-${HOME}/.nvm}/nvm.sh"
    # shellcheck disable=1091
    [[ -s "/usr/local/opt/nvm/nvm.sh" ]] && . "/usr/local/opt/nvm/nvm.sh";
}
command -v npm  >/dev/null 2>&1 || {
    log notice "Installing nodejs stable."
    nvm install stable
}
# Check if npm has permissions to install packages (system installed does not)
# Share https://stackoverflow.com/a/59227497/99834
test -w "$(npm config get prefix)" || {
    log warning "Your npm is not allowed to write to $(npm config get prefix), we will reconfigure its prefix"
    npm config set prefix "${HOME}/.local/"
}

if [[ -f yarn.lock ]]; then
    command -v yarn >/dev/null 2>&1 || {
        log warning "Installing missing yarn"
        npm install -g yarn
        yarn --version
    }
fi

# Create a build manifest so we can compare between builds and machines, this
# also has the role of ensuring that the required executables are present.
#
cat >out/log/manifest.yml <<EOF
system:
  uname: $(uname)
env:
  ARCH: ${ARCH:-null}  # taskfile
  OS: ${OS:-null}    # taskfile
  OSTYPE: ${OSTYPE:-null}
tools:
  bash: $(get_version bash)
  gh: $(get_version gh || echo null)
  git: $(get_version git)
  node: $(get_version node)
  npm: $(get_version npm)
  nvm: $(get_version nvm || echo null)
  pre-commit: $(get_version pre-commit)
  python: $(get_version python)
  task: $(get_version task)
  yarn: $(get_version yarn || echo null)
EOF

log notice "Install node deps using either yarn or npm"
if [[ -f yarn.lock ]]; then
    yarn install
else
    npm ci --no-audit
fi

[[ $ERR -eq 0 ]] && level=notice || level=error
log "${level}" "${0##*/} -> out/log/manifest.yml and returned ${ERR}"
exit "${ERR}"
