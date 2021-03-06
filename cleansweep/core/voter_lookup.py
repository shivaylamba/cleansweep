"""
A helper class to lookup voter by voter id
"""
import requests


def get_voter(voterid):
    """
    Gets voter details from our API using the voter id provided
    :param voterid: The voter id
    :return: JSON object with contains 'state', 'pb', 'ac' and 'voterid'
    """
    # voter-lookup service is no longer available
    return None
    # payload = {'voterid': voterid}
    # resp = requests.get("http://voter-lookup.missionvistaar.in/search", params=payload)
    # voter_data = resp.json()
    # if voter_data:
    #     d = voter_data[0]
    #     d['key'] = '{}/AC{:03d}/PB{:04d}'.format(d['state'], d['ac'], d['pb'])
    #     return voter_data[0]


def voterid_valid(voterid):
    """
    Just a more readable function to check if voter id is valid or not at the time of registration.

    Note: This function gets called in form validation. If any exception occurs the error gets displayed to user. Weird.
    """
    try:
        return get_voter(voterid)
    except Exception:
        return None
