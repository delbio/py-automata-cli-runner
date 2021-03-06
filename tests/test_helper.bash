load lib/assertions

export PY_AUTOMATA_CLI_RUNNER_TEST_DIR="${BATS_TMPDIR}/py-automata-cli-runner"
export PY_AUTOMATA_CLI_RUNNER_TMP_BIN="${PY_AUTOMATA_CLI_RUNNER_TEST_DIR}/bin"
export PY_AUTOMATA_CLI_RUNNER_CWD="${PY_AUTOMATA_CLI_RUNNER_TEST_DIR}/cwd"

export PATH="${BATS_TEST_DIRNAME}/libexec:$PATH"
export PATH="${BATS_TEST_DIRNAME}/../libexec:$PATH"
export PATH="${PY_AUTOMATA_CLI_RUNNER_TMP_BIN}:$PATH"

mkdir -p "${PY_AUTOMATA_CLI_RUNNER_TMP_BIN}"
mkdir -p "${PY_AUTOMATA_CLI_RUNNER_TEST_DIR}"
mkdir -p "${PY_AUTOMATA_CLI_RUNNER_CWD}"

setup() {
  cd "${PY_AUTOMATA_CLI_RUNNER_CWD}"
}

teardown() {
  rm -rf "${PY_AUTOMATA_CLI_RUNNER_TEST_DIR}"
}
