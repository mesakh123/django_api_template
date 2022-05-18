import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import propertyAPIService from "./propertyAPIService";


const initialState = {
    properties:[],
    property:{},
    isError:false,
    isLoading:false,
    isSuccess:false,
    message:''
}


// get all properties
export const getProperties = createAsyncThunk('properties/getAllProperties',
     async (_,thunkAPI) =>{
         try{
             return await propertyAPIService.getProperties();
         }
         catch(error){
             const message = (error.response && error.response.data&& error.response.data.message ) ||
             error.message || error.toString();
             return thunkAPI.rejectWithValue(message);
         }

})


export const propertySlice = createSlice({
    name: 'properties',
    initialState,
    reducers:{
        reset:(state)=>initialState
    },
    extraReducers:(builders)=>{
        builders
        .addCase(getProperties.pending, (state)=>{
            state.isLoading=true;
        })
        .addCase(getProperties.fulfilled, (state,action)=>{
            state.isLoading=false;
            state.isSuccess = true;
            state.properties=action.payload;
        })
        .addCase(getProperties.rejected, (state,action)=>{
            state.isLoading=false;
            state.isSuccess = true;
            state.properties=action.payload;
        })

    },
});

export const {reset} = propertySlice.actions;
export default propertySlice.reducer;
