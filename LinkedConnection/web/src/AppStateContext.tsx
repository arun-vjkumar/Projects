import React, {createContext, useContext, useReducer} from "react";
import {Connection} from "./components/types";


type Action =
    | {
    type: "INITIALIZE"
    payload: {
        connections: Connection[]
    }
} | {
    type: "GET_BY_NAME_LOCATION"
    payload: {
        connections: Connection[],
        name: string,
        location: string,
    }
} | {
    type: "GET_USER_CONNECTION",
    payload: {
        connections: Connection[],
        userId: number,
    }
} | {
    type: "GET_ALL_USERS",
    payload: {
        connections: Connection[]
    }
}

export interface AppState {
    connections: Connection[]
    name: string | null
    location: string | null
    userId: number | null
}


interface AppStateContextProps {
    state: AppState
    dispatch: React.Dispatch<Action>
}

const AppStateContext = createContext<AppStateContextProps>({} as AppStateContextProps)

const appStateReducer = (state: AppState, action: Action): AppState => {
    switch (action.type) {
        case "INITIALIZE": {
            return {
                ...state,
                connections: action.payload.connections
            }
        }

        case "GET_USER_CONNECTION": {
            return {
                ...state,
                connections: action.payload.connections,
                userId: action.payload.userId,
                location: null,
                name: null
            }
        }

        case "GET_BY_NAME_LOCATION": {
            return {
                ...state,
                connections: action.payload.connections,
                userId: null,
                location: action.payload.location,
                name: action.payload.name
            }
        }

        case "GET_ALL_USERS": {
            return {
                ...state,
                connections: action.payload.connections,
                userId: null,
                location: null,
                name: null
            }
        }

        default: {
            return state
        }
    }
}

const appData: AppState = {
    connections: [],
    userId: null,
    name: null,
    location: null
}


export const AppStateProvider = ({children}: React.PropsWithChildren<{}>) => {
    const [state, dispatch] = useReducer(appStateReducer, appData)

    return (
        <AppStateContext.Provider value={{state, dispatch}}>
            {children}
        </AppStateContext.Provider>
    )
}

export const useAppState = () => {
    return useContext(AppStateContext)
}
