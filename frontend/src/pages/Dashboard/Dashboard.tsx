import { Grid } from '@mui/material';
import { Box } from '@mui/system';
import React, { useState, useEffect, ReactNode } from 'react';
import styles from './Dashboard.module.css';
import SideBar from '../../components/SideBar/SideBar';
import { useDispatch, useSelector } from 'react-redux';
import { dashboardAsync } from '../../features/dashboard/dashboardThunk';
import { RootState } from '../../store/store';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';

interface PageWrapper {
  children?: ReactNode;
}

const Dashboard: React.FC<PageWrapper> = ({ children }) => {
  const [drawerOpen, setDrawerOpen] = useState(true);
  const user = useSelector((state: RootState) => state.auth.user);
  const dispatch = useDispatch();
  // useEffect(() => {
  //   if (user) {
  //     const dashboardData = {
  //       username: user.username,
  //       password: user.password,
  //     };
  //     (dispatch as any)(dashboardAsync(dashboardData))
  //       .unwrap()
  //       .then((response: any) => {
  //         dispatch(response.user);
  //       })
  //       .catch((error: any) => {});
  //   }
  // }, []);
  return (
    <>
      <Box component={'div'}>
        <SideBar
          open={drawerOpen}
          handleDrawerToggle={() => setDrawerOpen(!drawerOpen)}
        />
        <Grid container direction="column">
          {!drawerOpen && (
            <Grid className={styles.menuContainer} item>
              <IconButton aria-label="delete" size="small">
                <MenuIcon fontSize="inherit" />
              </IconButton>
            </Grid>
          )}
          <Grid container direction={'column'}>
            <Grid item>{children}</Grid>
          </Grid>
        </Grid>
      </Box>
    </>
  );
};

export default Dashboard;
