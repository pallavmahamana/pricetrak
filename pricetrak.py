from scrapers import FlipkartTracker, AmazonTracker
from config import URLS

class PriceTracker:
	trackers = []
	def __init__(self,urlsdict):
		for tracker in urlsdict:
			for url in urlsdict[tracker]:
				self.trackers.append(eval(tracker)(url))


	def print_trackers(self):
		print(self.trackers)


	def run_trackers(self):
		for tracker in self.trackers:
			print(tracker.get_product_name())
			print(tracker.get_price())

if __name__=='__main__':
	pricetracker = PriceTracker(URLS)
	pricetracker.run_trackers()




