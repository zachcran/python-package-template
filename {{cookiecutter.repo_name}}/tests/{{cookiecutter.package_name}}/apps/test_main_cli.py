from {{cookiecutter.package_name}}.apps import main_cli


def test_main_cli_version_flag(capsys):
    # 1. Arrange
    success_code = 0
    invalid_output = ""

    # 2. Act
    return_code = main_cli.main(["--version"])
    # Capture the printed text
    captured = capsys.readouterr()

    # 3. Assert
    # Successful return code
    assert return_code == success_code
    # stdout is not empty, meaning a version was provided; since version
    # will change frequently, we only check if *something* was output or not
    assert captured.out != invalid_output


def test_main_cli_normal_run(capsys):
    success_code = 0
    # Newline is a result of the `print()` call
    expected_output = "Hello World!\n"

    return_code = main_cli.main([])
    # Capture the printed text
    captured = capsys.readouterr()

    assert return_code == success_code
    assert captured.out == expected_output
