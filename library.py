class Library(object):
    """Holds shelves and prints all books on command."""
    shelfInstances = []
    def bookReport(self):
        """Print all books in library."""
        for obj in Library.shelfInstances:
            print obj
            print "I am holding %s" %str(obj.books)

class Shelf(Library):
    """Holds books."""
    def __init__(self,name):
        self.name = name
        Library.shelfInstances.append(self)
        self.books=[]
    def __repr__(self):
        return "I am the %s shelf." %self.name


class Book(Shelf):
    """May be put on or taken off a shelf."""
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return self.name
    def enshelf(self,aShelf):
        """Puts book on shelf"""
        aShelf.books.append(self)
    def unshelf(self,aShelf):
        """Takes book off shelf."""
        aShelf.books.remove(self)
        print "You removed %s" %str(self)


nathansLibrary = Library()

classicsShelf = Shelf("Classics")
warAndPeace = Book("War And Peace")
crimeAndPunish = Book("Crime And Punishment")
warAndPeace.enshelf(classicsShelf)
crimeAndPunish.enshelf(classicsShelf)

sciFiShelf = Shelf("Sci Fi")
endersGame = Book("Ender's Game")
harshMoon = Book("The Moon is a Harsh Mistress")
endersGame.enshelf(sciFiShelf)
harshMoon.enshelf(sciFiShelf)

nathansLibrary.bookReport()

harshMoon.unshelf(sciFiShelf)

nathansLibrary.bookReport()
