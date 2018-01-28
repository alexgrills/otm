from unittest import mock
import request_number_service
import pytest
import json

@pytest.fixture
def mock_service():
	request_number_service.app.testing = True
	return request_number_service.app.test_client()

def test_can_get_random_number_between_one_and_one_million():
	number = request_number_service.one_to_one_million()
	assert 1 < number and number < 1_000_000

def test_can_handle_get_number_request(mock_service, mocker):
	mock_requests = mocker.patch('requests.get', return_value = json.dumps({'success': True}))
	mock_random_number = mocker.patch('request_number_service.one_to_one_million', return_value=1)
	response = mock_service.get('/get_a_number')
	expected_json = {
		'number': 1
	}
	assert response.status_code == 200
	assert json.loads(response.data) == expected_json
	mock_requests.assert_called_once_with('https://database_service/update_number?number=1')

def test_can_handle_get_number_request_when_no_spins_are_available(mock_service, mocker):
	mock_requests = mocker.patch('requests.get', return_value = json.dumps({'success': False}))
	mock_random_number = mocker.patch('request_number_service.one_to_one_million', return_value=1)
	response = mock_service.get('/get_a_number')
	expected_json = {
		'number': -1
	}
	assert response.status_code == 200
	assert json.loads(response.data) == expected_json
	mock_requests.assert_called_once_with('https://database_service/update_number?number=1')