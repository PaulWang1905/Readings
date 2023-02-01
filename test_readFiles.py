from readFiles import readEntries as read


class test_readEntries:
    def test_readEntries(self):
        files = read('category')
        for file in files:
            assert file.read_date != None
            assert file.title != None
            assert file.link != None
            assert file.authors != None
            # file.comments could be None
            # do not need the line: assert file.comments != None
            assert file.date != None
            # assert file.tags != None
            # for the moment, I do not need to test the tags

if __name__ == "__main__":
    print("Testing readEntries")
    test_readEntries().test_readEntries()
    print("All tests passed")