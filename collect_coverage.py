import coverage
import test_sut

cov = coverage.Coverage()
cov.set_option("run:branch", True)
cov.start()

test_sut.test_handle_event()

cov.stop()
cov.save()
cov.report(show_missing=True)