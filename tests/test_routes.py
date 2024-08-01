def test_home_page():
    response = client.get('/')
    assert response.status_code == 200
