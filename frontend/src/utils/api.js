import axios from 'axios';
import { API_BASE_URL } from './constants';

export async function getQueryResponse(req) {
	return await axios.post(`${API_BASE_URL}/query`, req)
}

export async function getUpdatedFilter(req) {
	return await axios.post(`${API_BASE_URL}/filter_topics`, req)
}