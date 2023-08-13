import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  isAuthenticated: false,
  user: {
    id: null,
    username: '',
  },
  token: '',
};

const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    login: (state, action) => {
      state.isAuthenticated = true;
      state.user = {
        id: action.payload.id,
        username: 'action.payload.username',
      };
      state.token = action.payload.token;
    },
    logout: (state) => {
      state.isAuthenticated = false;
      state.user = { id: null, username: '' };
      state.token = '';
    },
  },
});

export const { login, logout } = authSlice.actions;

export default authSlice.reducer;
