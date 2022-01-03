import json

class PaperService():
    def __init__(self):
        file = open('res/papers.json')
        data = json.load(file)
        self.papers = data['papers']
    
    def findBySize(self, size):
        return list(map(self._toString, filter(lambda p: p['size'] == size, self.papers)))
    
    def findByColor(self, color):
        return list(map(self._toString, filter(lambda p: p['color'] == color, self.papers)))
    
    def findLargestPapers(self):
        # Current complexity O(n*t)
        # * n beign number of papers
        # * t beign number type of papers

        largest_paper_types = []
        largest_paper_sizes = []
        largest_papers = []
        for paper in self.papers:
            paper_type = paper['size'][0]
            paper_size = int(paper['size'][-1])
            if paper_type not in largest_paper_types:
                largest_paper_types.append(paper_type)
                largest_paper_sizes.append(paper_size)
                largest_papers.append(paper)
            else:
                i = largest_paper_types.index(paper_type)
                if paper_size > largest_paper_sizes[i]:
                    largest_paper_types[i] = paper_type
                    largest_paper_sizes[i] = paper_size
                    largest_papers[i] = paper

        return map(self._toString, largest_papers)

    def _toString(self, paper):
        id = paper['id']
        size = paper['size']
        color = paper['color']
        return f'{id}) {size} {color}'