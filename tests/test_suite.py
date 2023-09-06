from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from .test_generate_password import TestGenererMotsDePasse
from .test_input import TestInput
from .test_tkinter import TestTkinter

test_password = TestLoader().loadTestsFromTestCase(TestGenererMotsDePasse)
test_tkinter = TestLoader().loadTestsFromTestCase(TestTkinter)
test_input = TestLoader().loadTestsFromTestCase(TestInput)

suite = TestSuite([test_password, test_input, test_tkinter])

HTMLTestRunner(output='report_testing', combine_reports=True, report_name="index", add_timestamp=False).run(suite)