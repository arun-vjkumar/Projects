import React, {useEffect, useState} from "react"
import {useAppState} from "../AppStateContext"
import DataTable, {createTheme} from "react-data-table-component"
import {Connection} from "./types"
import {get, getConnectionByNameLocation, getConnectionByUserId, getConnections} from "../Requests"
import styled from "styled-components"

const DisplayBox = styled.div`
width: 80%;
margin: 20px;
padding-left: 10px;
margin-left:auto; 
margin-right:auto;
text-align: center;
align: center;
top: 10px;
`

const StyledSpan = styled.span`
margin: 10px;
padding: 5px:
`

createTheme('light', {
    text: {
        primary: '#268bd2',
        secondary: '#1c1818',
    },
    context: {
        background: '#cb4b16',
        text: '#FFFFFF',
    },
    divider: {
        default: '#073642',
    },
    action: {
        button: 'rgba(0,0,0,0.54)',
        hover: 'rgba(0,0,0,.08)',
        disabled: 'rgba(0,0,0,.12)',
    },
});

const customStyles = {
    header: {
        style: {
            fontSize: '22px'
        },
    },
    headRow: {
        style: {
            minHeight: '56px',
            borderBottomWidth: '1px',
            border: '1px solid black',
        },
    },
    headCells: {
        style: {
            color: '#202124',
            fontSize: '14px',
            border: "5px",
            outline: '1px solid #FFFFFF',
            borderLeft: '1px solid black',
            borderBottom: '1px solid black',
        },
    },
    cells: {
        style: {
            borderLeft: '1px solid black',
        },
    },
    rows: {
        highlightOnHoverStyle: {
            backgroundColor: 'rgb(230, 244, 244)',
            borderBottomColor: '#FFFFFF',
            borderRadius: '25px',
            outline: '1px solid #FFFFFF',
            border: '2px solid black',
        },
    },
    table: {
        style: {
            borderBottomWidth: '1px',
            border: '1px solid black',
        },
    }
};

const columns = [
    {
        name: 'UserId',
        selector: (row: Connection) => row.userId,
        width: "100px"
    },
    {
        name: 'Name',
        selector: (row: Connection) => row.name
    },
    {
        name: 'Location',
        selector: (row: Connection) => row.location
    },
];

export const Connections = () => {
    const {state} = useAppState()
    const {dispatch} = useAppState()
    const [searchByNameLocation, setSearchByNameLocation] = useState(false)
    const [name, setName] = useState()
    const [location, setLocation] = useState()
    const [userId, setUserId] = useState()
    const [maxPage, setMaxPageNo] = useState(0)
    const [page, setPageNo] = useState(1)
    useEffect(() => {
        getAllUsers()
    }, [page])

    async function getByName() {
        const connections = await getConnectionByUserId(userId);
        if (connections) {
            dispatch({type: "GET_USER_CONNECTION", payload: {connections: Object.values(connections), userId: userId}})
        }
    }

    async function initialize() {
        await get("initialize", {numUsers: 100})
        getNewUsers()
    }

    async function getByNameLocation() {
        if (!name && !location) {
            alert("either name or location should be entered")
        } else {
            const connections = await getConnectionByNameLocation(name, location);
            if (connections) {
                dispatch({
                    type: "GET_BY_NAME_LOCATION",
                    payload: {connections: Object.values(connections), name: name, location: location}
                })
            }
        }
    }

    async function getAllUsers() {
        if (page > maxPage) {
            let connections = await getConnections(page)
            if (page > 1) {
                connections = [...state.connections, ...connections]
            }
            if (connections) {
                dispatch({
                    type: "GET_ALL_USERS",
                    payload: {connections: Object.values(connections)}
                })
                setMaxPageNo(page)
            }
        }
    }

    function getNewUsers() {
        setPageNo(1)
        setMaxPageNo(0)
        getAllUsers()
    }

    function getSearchParameter(value: string) {
        if (value === "userId")
            setSearchByNameLocation(false)
        else
            setSearchByNameLocation(true)
    }


    return (
        <DisplayBox>
            <div style={{margin: "10px"}}>
                <select onChange={event => getSearchParameter(event.target.value)}>
                    <option value="userId"> UserId</option>
                    <option value=""> Search By Name or Location</option>
                </select>
                {
                    !searchByNameLocation &&
                    <StyledSpan>
                        <input name={"userId"} onChange={(event => setUserId(event.target.value))}
                               placeholder={"User Id"}/>
                        <button onClick={getByName}> Search</button>
                    </StyledSpan>
                }
                {
                    searchByNameLocation &&
                    <StyledSpan>
                        <input type="text" onChange={(event => setName(event.target.value))} placeholder={"Name"}/>
                        <input name={"location"} onChange={(event => setLocation(event.target.value))}
                               placeholder={"Location"}/>
                        <button onClick={getByNameLocation}> Search</button>
                    </StyledSpan>
                }
                <StyledSpan>
                    <button onClick={getNewUsers}> Fetch All </button>
                    <button onClick={initialize}> Generate Connections</button>
                </StyledSpan>
            </div>

            <DataTable<Connection>
                theme="light"
                columns={columns}
                paginationPerPage={10}
                data={state.connections}
                customStyles={customStyles}
                pagination={true}
                paginationRowsPerPageOptions={[10]}
                onChangePage={setPageNo}
            />
        </DisplayBox>
    )
}
