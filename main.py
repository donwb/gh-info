from github import Github
import os

def getUsers():
	g = Github(os.environ['API_KEY'])
	org = g.get_organization('turnercode')
	print(org)
	
	# you can get repos w/get_repos()
	
	teams = org.get_teams()
	team = [t for t in teams if t.name == 'cARB'][0]
	# print([m.login for m in team.get_members()])
	
	for m in team.get_members():
		c = [e for e in m.get_events()]
		if len(c) == 0:
			login = m.login
			real_name = 'No Real Name Provided' if m.name == None else m.name
			print('{r} ({l}) has no events in the cARB team'.format(l=login, r=real_name))


if __name__ == '__main__':
	getUsers()
	