import { useEffect, useState } from 'react';
import ListOf from '../../components/ListOf/ListOf';
import Grid from '@mui/material/Grid';
import Dashboard from '../Dashboard/Dashboard';
import { useLocation } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { getAllOfficeManagersAsync } from '../../features/officemanager/officemanagerThunk';
import { getAllSchoolsAsync } from '../../features/school/schoolThunk';
import { getAllProfessorsAsync } from '../../features/professor/professorThunk';
import { getAllTeachersAsync } from '../../features/teacher/teacherThunk';
import { getAllstudentsAsync } from '../../features/student/studentThunk';
import { getAllOfficeManagers } from '../../features/officemanager/officemanagerSlice';
import { getAllProfessors } from '../../features/professor/professorSlice';
import { getAllSchools } from '../../features/school/schoolSlice';
import { getAllstudents } from '../../features/student/studentSlice';
import { getAllTeachers } from '../../features/teacher/teacherSlice';
import styles from './Lists.module.css';
import { useSelector } from 'react-redux';
import { RootState } from '../../store/store';
import { useParams } from 'react-router-dom';

const List = () => {
  const { userType } = useParams();
  const location = useLocation();
  const dispatch = useDispatch();

  const allOfficeManagers = useSelector(
    (state: RootState) => state.officeManager.allOfficeManagers
  );
  const allProfessors = useSelector(
    (state: RootState) => state.professor.allProfessors
  );
  const allSchools = useSelector((state: RootState) => state.school.allschools);

  const allTeachers = useSelector(
    (state: RootState) => state.teacher.allteachers
  );
  const allStudents = useSelector(
    (state: RootState) => state.student.allstudents
  );

  useEffect(() => {
    (dispatch as any)(getAllOfficeManagersAsync({}))
      .unwrap()
      .then((response: any) => {
        dispatch(getAllOfficeManagers(response));
      })
      .catch((error: any) => {});

    (dispatch as any)(getAllSchoolsAsync({}))
      .unwrap()
      .then((response: any) => {
        dispatch(getAllSchools(response));
      })
      .catch((error: any) => {});

    (dispatch as any)(getAllProfessorsAsync({}))
      .unwrap()
      .then((response: any) => {
        dispatch(getAllProfessors(response));
      })
      .catch((error: any) => {});

    (dispatch as any)(getAllstudentsAsync({}))
      .unwrap()
      .then((response: any) => {
        dispatch(getAllstudents(response));
      })
      .catch((error: any) => {});

    (dispatch as any)(getAllTeachersAsync({}))
      .unwrap()
      .then((response: any) => {
        dispatch(getAllTeachers(response));
      })
      .catch((error: any) => {});
  }, []);
  const putRightListOnScreen = () => {
    return userType.trim() === 'officemanagers' ? (
      <Grid container spacing={2} className={styles.grid}>
        {allOfficeManagers.map((office_manager: any, index) => {
          return (
            <Grid item xs={12} sm={6} md={4} lg={3}>
              <ListOf
                type="officemanager"
                username={office_manager.username}
                id={office_manager.id}
              />
            </Grid>
          );
        })}{' '}
      </Grid>
    ) : userType.trim() === 'professors' ? (
      <Grid container spacing={2} className={styles.grid}>
        {allProfessors.map((professor: any, index) => {
          return (
            <Grid item xs={12} sm={6} md={4} lg={3}>
              <ListOf
                type="professor"
                username={professor.username}
                id={professor.id}
              />
            </Grid>
          );
        })}{' '}
      </Grid>
    ) : userType.trim() === 'schools' ? (
      <Grid container spacing={2} className={styles.grid}>
        {allSchools.map((school: any, index) => {
          return (
            <Grid item xs={12} sm={6} md={4} lg={3}>
              <ListOf type="school" username={school.username} id={school.id} />
            </Grid>
          );
        })}{' '}
      </Grid>
    ) : userType.trim() === 'teachers' ? (
      <Grid container spacing={2} className={styles.grid}>
        {allTeachers.map((teacher: any, index) => {
          return (
            <Grid item xs={12} sm={6} md={4} lg={3}>
              <ListOf
                type="teacher"
                username={teacher.username}
                id={teacher.id}
              />
            </Grid>
          );
        })}{' '}
      </Grid>
    ) : userType.trim() === 'students' ? (
      <Grid container spacing={2} className={styles.grid}>
        {allStudents.map((student: any, index) => {
          return (
            <Grid item xs={12} sm={6} md={4} lg={3}>
              <ListOf
                type="student"
                username={student.username}
                id={student.id}
              />
            </Grid>
          );
        })}{' '}
      </Grid>
    ) : (
      <></>
    );
  };
  return <Dashboard>{putRightListOnScreen()}</Dashboard>;
};

export default List;
