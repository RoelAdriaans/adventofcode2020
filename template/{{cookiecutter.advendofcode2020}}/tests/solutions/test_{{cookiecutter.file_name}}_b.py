import pytest

from solutions.{{cookiecutter.file_name}} import {{cookiecutter.class_name}}PartB


class Test{{cookiecutter.class_name}}PartB:
    @pytest.mark.skip("This code is not yet implemented.")
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_{{cookiecutter.file_name}}b_solve(self, input_data, expected_result):
        solution = {{cookiecutter.class_name}}PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    @pytest.mark.skip("This code is not yet implemented.")
    def test_{{cookiecutter.file_name}}b_data(self):
        """ Result we got when we did the real solution """
        solution = {{cookiecutter.class_name}}PartB()
        res = solution("{{cookiecutter.directory_name}}/{{cookiecutter.file_name}}.txt")
        assert res == 0
