from readFiles import readEntries as read


class test_readEntries:
    def test_readEntries(self):
        files = read('category')
        # files is a list of objects
        # each object is a file
        # each file has the following attributes:
        # read_date, title, link, authors, comments, date, tags
        for file in files:
            assert file.read_date != None
            assert file.title != None
            assert file.link != None
            assert file.authors != None
            assert file.uri != None
            assert file.date != None
            # file.comments could be None
            # do not need the line: assert file.comments != None
            # no need to test assert file.tags != None
            # for the moment, I do not need to test the tags

if __name__ == "__main__":
    print("Testing readEntries function")
    test_readEntries().test_readEntries()
    #print(test_readEntries.__dict__)
    print("All tests passed")