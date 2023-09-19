#this is an unused import, but we can define it once here in the unit_base_test file and then import UnitBaseTest class into all unit tests. That was the unused import is only defined once instead of defining from app import app in every unit test file.
#importing app is important because it gives us access to the store model which is needed for the item unit tests to have knowledge of the the store model.
#theoretically, the existing base_test could have been used, but since that script has setup and teardown methods that create a new database and remove the database with each test (which isn't needed for the unittests) it takes longer to run.
from app import app
from unittest import TestCase

#this is setting up the UnitBaseTest class which currently isn't being used; however, it lets us import app into all unittests 
class UnitBaseTest(TestCase):
    pass