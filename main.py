import scrape
import parse

if __name__ == "__main__":
    #eventbrite webscrape
    #https://www.eventbrite.com/d/philippines--makati-city/events/?crt=regular&page=1&slat=14.5547&slng=121.0244&sort=best

    for i in range(1):
        data = scrape.scrape_eventbrite("https://www.eventbrite.com/d/philippines--makati-city/events/?crt=regular&page="+str(i+1)+"&slat=14.5547&slng=121.0244&sort=best")

        for i in range(len(data["eventsCollection"])):
            parse.parseMeeting(data, i)
