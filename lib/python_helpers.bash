python_i=python
python_pip=pip

function setPythonVersion() {
    # https://stackoverflow.com/a/677212
    if command -v python3 >/dev/null 2>&1; then
        python_i=python3
        python_pip=pip3
    else
        python_i=python
        python_pip=pip
    fi
}