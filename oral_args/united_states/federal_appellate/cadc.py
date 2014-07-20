"""Scraper for D.C. Circuit of Appeals
CourtID: cadc
Court Short Name: cadc
Author: Andrei Chelaru
Reviewer:
Date created: 18 July 2014
"""

from datetime import datetime, date

from juriscraper.OralArgumentSite import OralArgumentSite


class Site(OralArgumentSite):
    def __init__(self):
        super(Site, self).__init__()
        self.court_id = self.__module__
        d = date.today()
        self.url = 'http://www.cadc.uscourts.gov/recordings/recordings.nsf/DocsByRDate?OpenView&count=100&SKey={yearmo}'.format(
            yearmo=d.strftime('%Y%m')
        )

    def _get_download_urls(self):
        path = "id('ViewBody')//div[contains(concat(' ',@class,' '),' row-entry')]//@href"
        return list(self.html.xpath(path))

    def _get_case_names(self):
        path = "id('ViewBody')//*[contains(concat(' ',@class,' '),' column-two')]/div[1]/text()"
        return list(self.html.xpath(path))

    def _get_case_dates(self):
        path = "id('ViewBody')//date/text()"
        return map(self._return_case_date, self.html.xpath(path))

    @staticmethod
    def _return_case_date(e):
        e = ''.join(e.split())
        return datetime.strptime(e, '%m/%d/%Y').date()

    def _get_docket_numbers(self):
        path = "id('ViewBody')//*[contains(concat(' ',@class,' '),' row-entry')]//a//text()"
        return list(self.html.xpath(path))