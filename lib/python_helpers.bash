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

function installPythonDeps() {
    setPythonVersion
    ${PYTHON_PIP} install -r ${BASE_LIB_FOLDER}/requirements.txt
}

PYTHON_DEPS_ON_SYNC="true"
LOCAL_DEPS_STORE_FILE=${BASE_LIB_FOLDER}/local.deps.store.lastmodification
SOURCE_DEPS_STORE_FILE=${BASE_LIB_FOLDER}/source.deps.store.lastmodification

function isPythonDepsOnSync() {

    if [ -f $LOCAL_DEPS_STORE_FILE ]; then
        # if local and source differ then python deps out of sync
        cmp -s ${LOCAL_DEPS_STORE_FILE} ${SOURCE_DEPS_STORE_FILE} || PYTHON_DEPS_ON_SYNC="false"
    else
        # if local deps store not exist python deps out of sync
        PYTHON_DEPS_ON_SYNC="false"
    fi
}

function commitOnSync() {
    cp ${SOURCE_DEPS_STORE_FILE} ${LOCAL_DEPS_STORE_FILE} 
}