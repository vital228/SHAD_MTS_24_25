import scrapy


class KinoriumSpider(scrapy.Spider):
    name = "kinorium"
    allowed_domains = ["ru.kinorium.com"]
    # start_urls = ["https://ru.kinorium.com/collections/kinorium/327/?order=sequence&page=1&perpage=200&show_viewed=1"]

    def start_requests(self):
        urls = [f"https://ru.kinorium.com/collections/kinorium/327/?order=sequence&page={i}&perpage=200&show_viewed=1" for i in range(1, 6)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for selector in response.css(".filmList__item-content"):
            title = selector.css(".title::text").get()
            genre = selector.css(".filmList__extra-info::text").get()
            if genre:
                genre = genre[:genre.rfind(",")]
            director = selector.css(".filmList__extra-info-director > a::text").get()
            country = selector.css(".filmList__extra-info-director::text").get()
            country = country[:-3]
            year = selector.css(".filmList__small-text::text").get()
            if year:
                year = year[year.rfind(",") + 2:]
            rating = selector.css(".rating_imdb > span::text").get()
            yield {
                "Название": title,
                "Жанр": genre,
                "Режиссер": director,
                "Страна": country,
                "Год": year,
                "IMDB": rating,
            }
        # next_page = response.css("a.next_page::attr(href)").get()
        # if next_page:
        #     yield response.follow(next_page, callback=self.parse)

