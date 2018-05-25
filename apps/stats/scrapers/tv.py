from datetime import datetime

from .base import Scraper
from apps.stats.models import Fixture
import pytz


class TVScraper(Scraper):
    channels = {'star-sports-india': 'Star Sports 1',
                'star-sports-2-india': 'Star Sports 2',
                'star-sports-3-india': 'Star Sports 3',
                'star-sports-4-india': 'Star Sports 4',
                'star-sports-hd-1-india': 'Star Sports HD 1',
                'star-sports-hd-2-india': 'Star Sports HD 2',
                'sony-six-india': 'Sony Six',
                'sony-six-hd-india': 'Sony Six HD',
                'sony-kix-india': 'Sony Kix',
                'ten-sports': 'TEN Sports',
                'ten-action': 'Ten Action',
                # 'mutv-online': 'MUTV Online',
                }

    url = 'https://www.livesoccertv.com/teams/england/manchester-united/'

    # def scrape(self):
    #     json_data = self.get_json_from_url(
    #         'https://www.livesoccertv.com/m/api/teams/england/manchester-united/?iso_code=np')
    #     if 'fixtures' in json_data:
    # 
    #         for fixture in json_data['fixtures']:
    #             timestamp = float(fixture.get('timestamp'))
    #             self.data[timestamp] = []
    #             channels = fixture.get('channels')
    #             for channel in channels:
    #                 if channel.get('slug') in self.channels:
    #                     self.data[timestamp].append(self.channels.get(channel.get('slug')))
    #                     # continue
    #             if not self.data[timestamp]:
    #                 del self.data[timestamp]
    def scrape(self):
        root = self.get_root_tree()
        if root is not None:
            match_rows = root.cssselect('.matchrow')
            for match_row in match_rows:
                # skip past matches
                if match_row.cssselect('.narrow.ft'):
                    continue
                try:
                    timestamp = float(match_row.cssselect('span.ftime span.ts')[0].get('dv')) / 1000
                    self.data[timestamp] = []
                    channels_text = match_row.cssselect('td')[-1].text_content()
                    channel = channels_text.split(',')[0]
                    self.data[timestamp].append(channel)
                except IndexError:
                    pass

    def save(self):
        for timestamp, channels in self.data.items():
            dt = datetime.utcfromtimestamp(timestamp).replace(tzinfo=pytz.UTC)
            try:
                fixture = Fixture.objects.get(datetime=dt)
                if not fixture.broadcast_on:
                    fixture.broadcast_on = ', '.join(channels)
                    fixture.save()
            except Fixture.DoesNotExist:
                pass
