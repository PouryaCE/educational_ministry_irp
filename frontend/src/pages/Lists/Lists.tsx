import React, { useEffect } from 'react';
import ListOf from '../../components/ListOf/ListOf';
import Grid from '@mui/material/Grid';
import Dashboard from '../Dashboard/Dashboard';
import { useLocation } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { getAllOfficeManagersAsync } from '../../features/officemanager/officemanagerThunk';
import { createschoolAsync } from '../../features/school/schoolThunk';
import { getProfessorsAsync } from '../../features/professor/professorThunk';
import { getstudentAsync } from '../../features/student/studentThunk';
import styles from './Lists.module.css';

const List = () => {
  const location = useLocation();
  const dispatch = useDispatch();
  const pathname = location.pathname;
  const modelPathArray = pathname.split('/');
  const getterBase = modelPathArray[modelPathArray.length - 1];
  useEffect(() => {
    (dispatch as any)(getAllOfficeManagersAsync({}))
      .unwrap()
      .then((response: any) => {
        console.log('hello list officemanagers: ', response);
        // dispatch(response.user);
      })
      .catch((error: any) => {});
    (dispatch as any)(createschoolAsync({}))
      .unwrap()
      .then((response: any) => {
        console.log('hello list schools: ', response);
        // dispatch(response.user);
      })
      .catch((error: any) => {});

    (dispatch as any)(getProfessorsAsync({}))
      .unwrap()
      .then((response: any) => {
        console.log('hello list schools: ', response);
        // dispatch(response.user);
      })
      .catch((error: any) => {});

    (dispatch as any)(getstudentAsync({}))
      .unwrap()
      .then((response: any) => {
        console.log('hello list schools: ', response);
        // dispatch(response.user);
      })
      .catch((error: any) => {});
  }, []);
  return (
    <Dashboard>
      <Grid container spacing={2} className={styles.grid}>
        <Grid item xs={12} sm={6} md={4} lg={3}>
          <ListOf />
        </Grid>
        {/* <Grid item xs={12} sm={2} md={4} lg={3}>
          <ListOf />
        </Grid>
        <Grid item xs={12} sm={6} md={4} lg={3}>
          <ListOf />
        </Grid>
        <Grid item xs={12} sm={6} md={4} lg={3}>
          <ListOf />
        </Grid>
        <Grid item xs={12} sm={6} md={4} lg={3}>
          <ListOf />
        </Grid>
        <Grid item xs={12} sm={6} md={4} lg={3}>
          <ListOf />
        </Grid> */}
      </Grid>
    </Dashboard>
  );
};

export default List;
