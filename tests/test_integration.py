def test_integration():
    response = client.get('/integration')
    assert response.status_code == 200
