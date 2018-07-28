#!/usr/bin/env bats

load test_helper

@test "without args, show help for root py-automata-cli-runner command" {
  run py-automata-cli-runner-help

  assert_success

  assert_line "Usage: py-automata-cli-runner <command> [<args>]"
}

@test "shows help for a specific command" {
  cat > "${PY_AUTOMATA_CLI_RUNNER_TMP_BIN}/py-automata-cli-runner-hello" <<SH
#!shebang
# Usage: py-automata-cli-runner hello <world>
# Summary: Says "hello" to you
# This command is useful for saying hello.
echo hello
SH

  run py-automata-cli-runner-help hello

  assert_success
  assert_output <<SH
Usage: py-automata-cli-runner hello <world>

This command is useful for saying hello.
SH
}
