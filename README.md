# [covidwith.tech](https://covidwith.tech)

A bot who can give news and stats about covid-19 and also provide mental help.

Covid-19 is our new reality. We are all in in this together and need each other to go through difficult times. These times fake news may cause anxiety.

# What is it?

We made a bot, Covid-19 Buddy, for you to feel comfortable to talk to. Ask your Buddy about current Covid-19 cases, tell your Buddy to verify URL source and ask for mental support. We got your back.
# Why?

Primarily, we care about you and your wellbeing. We use WhatsApp because it is accessible for all. There are many resources, but nowhere you can easily obtain this information without being overwhelmed. Besides, we have all significant resources in one.

# How can I use it?

To begin, connect to your bot by sending a WhatsApp message from your device to [+1 415 523 8886](https://wa.me/14155238886) (click the number to open WhatsApp) with the text join think-our. After that, you can start interacting with the bot (a Hello it's a good start).
## FAQ
### Why to choose Covid-19 Buddy?

> Covid-19 Buddy helps you to find answers to many questions regarding current Covid-19 situation.

### How Covid-19 Buddy is built?

> Covid-19 Buddy uses the [Twilio API for WhatsApp](https://www.twilio.com/whatsapp) to send and receive the WhatsApp messages. For the speech recognition we used [Twilio Autopilot](https://www.twilio.com/autopilot) and for the web app we used [Flask](https://github.com/pallets/flask/) micro framework.
>
> The info we provide, news and stats are given by [NewsAPI](https://newsapi.org/) and [Covid-19 API](https://covid19api.com/), respectively.

### How does Covid-19 Buddy recognize my country?

> Covid-19 Buddy automatically detects country by the international code of your number, but you can also ask for a specific country, just tell it; e.g, How is Mexico doing with covid?

### Can I trust to the provided news about Covid-19?

> Yes, Covid-19 Buddy uses verified information and can even check URL source provided by you to avoid freud.


## Instalation
We use Python 3.8 and `pipenv` to manage the dependencies. Install with `pipenv install`.

## Run
Activate the `pipenv shell` and run `flask run`.

## See it live in [https://covidwith.tech](https://covidwith.tech)

# This project was made for the [MHacks 13 beta](https://mhacks-13-beta.devpost.com/) hackaton. 