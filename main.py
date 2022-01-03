from lib.services.paperService import PaperService
import pprint


def main():
    """
    This function should 
     * find a paper by color
     * then find by size
     * then all largests for each type

    > Do not change this file
    """
    paperService = PaperService()

    # Color
    color = input('Select a paper color: ')
    papers = paperService.findByColor(color.upper())

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint([str(p) for p in papers])

    # Size
    size = input('Select a paper size: ')
    papers = paperService.findBySize(size.upper())

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint([str(p) for p in papers])

    # Largest ones
    print('Getting all largest papers for each type')
    papers = paperService.findLargestPapers()

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint([str(p) for p in papers])


if __name__ == '__main__':
    main()