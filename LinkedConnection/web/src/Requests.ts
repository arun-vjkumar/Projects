import axios from "axios"
import {Connection} from "../components/types";
const API_URl = "http://localhost:8000"

export async function get(subUrl: string, query?: {[key: string]: any}) {
    return axios({
        method: 'get',
        url: `${API_URl}/${subUrl}`,
        params: query,
    })
}

export async function getConnections(pageNo: number): Promise<Connection[]> {
    const res = await get("connections", {page: pageNo, pageSize: 11})
    return res.data["connections"]
}

export async function getConnectionByUserId(userId: number): Promise<Connection[]> {
    if (!userId) {
        alert(`please enter proper userId: ${userId}`)
    }
    const res = await get("userConnection", {userId: userId})
    return res.data["connections"]
}

export async function getConnectionByNameLocation(name: string, location: string) {
    if (!name) {
        const res = await get("connectionByNameLocation", {name: name})
        return res.data["connections"]
    }

    if (!location) {
        const res = await get("connectionByNameLocation", {location: location})
        return res.data["connections"]
    }
}
