import json

class TestAPICase():
    def test_welcome(self, api):
        res = api.get('/')
        assert res.status == '200 OK'
        assert res.json['message'] == "Welcome to my Flask API for snooker players!"

    def test_index(self, api):
        res = api.get('/api/players')
        assert res.status == '200 OK'
        assert len(res.json) == 2

    def test_show(self, api):
        res = api.get('/api/players/1')
        assert res.status == '200 OK'
        assert res.json["name"] == 'Test Player1'

    def test_create(self, api):
        mock_data = json.dumps({"name": 'Test Player3'})
        mock_headers = { 'Content-Type': 'application/json'}
        res = api.post('api/players', data=mock_data, headers = mock_headers)
        assert res.status == '201 CREATED'
        assert res.json["id"] == 3
        assert res.json["name"] == 'Test Player3'

    def test_find_by_id_error(self, api):
        res = api.get('/api/players/4')
        assert res.status == '400 BAD REQUEST'
        assert "do not have records" in res.json['message']
    
    def test_update(self, api):
        mock_data = json.dumps({"nationality": 'Test_Nation_1', "stats":{"world_titles": 1, "world_ranking": 1}})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.patch('/api/players/1', data=mock_data, headers=mock_headers)
        assert res.json["stats"]["world_titles"] == 1
        assert res.json["stats"]["world_ranking"] == 1
        assert res.json["nationality"] == "Test_Nation_1"

    # def test_delete_cat(self, api):
    #     res = api.delete('/api/cats/1')
    #     assert res.status == '204 NO CONTENT'

    def test_not_found(self, api):
        res = api.get('/notaroute')
        assert res.status == '404 NOT FOUND'
        assert 'Oops!' in res.json['message']

    # def test_server_error(self, api):
    #     res =  ...
    #     assert res.status == '500 INTERNAL SERVER ERROR'
    #     assert 'It\'s not you' in res.json["message"] 