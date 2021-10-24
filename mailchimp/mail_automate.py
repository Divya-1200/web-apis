import mailchimp_transactional as MailchimpTransactional
from mailchimp_transactional.api_client import ApiClientError
from decouple import config

API_KEY = config('API_KEY')

print(API_KEY)


def run():
  try:
    mailchimp = MailchimpTransactional.Client('API_KEY')
    print(mailchimp)
    response = mailchimp.users.ping()
    # print( mailchimp.users.ping())
    # print(response)
    print('API called successfully: {}'.format(response))
  except ApiClientError as error:
    print('An exception occurred: {}'.format(error.text))


if __name__ == "__main__":
  run()