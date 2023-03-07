from function import git_repo
import unittest

#  git_repo function is being tested. This script has 3 testcases.

class test_repo(unittest.TestCase):

    def testcase1(self): #  Here assertEqual is being used and the git_repo function returns true when it is able to connect with git user id DhruviPatel157 and then display repositories and number of commits
        self.assertEqual(git_repo('DhruviPatel157'), True, 'True')

    def testcase2(self):#  Here asserNotEqual is being used and the git_repo function returns false as it is not able to connect with dhruvi
        self.assertNotEqual(git_repo('dhruvi'), False, 'False')

    def testcase3(self):#  Here asserNotEqual is being used and the git_repo function returns false as it is not able to connect with dhruvi
        self.assertNotEqual(git_repo('dhruvipatel157'), False, 'False')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

