import React from "react";

export const AppStateProvider = ({children}: React.PropsWithChildren<{}>) => {
    return (
        <AppStateContext.Provider value={}>
            {children}
            </AppStateContext.Provider>)

}
