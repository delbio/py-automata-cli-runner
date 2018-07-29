PYTHON_I=python
PYTHON_PIP=pip

function setPythonVersion() {
    # https://stackoverflow.com/a/677212
    if command -v python3 >/dev/null 2>&1; then
        PYTHON_I=python3
        PYTHON_PIP=pip3
    else
        PYTHON_I=python
        PYTHON_PIP=pip
    fi
}