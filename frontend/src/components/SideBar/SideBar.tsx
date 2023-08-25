import React from "react";
import { Box } from "@mui/system";
import Drawer from "@mui/material/Drawer";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemText from "@mui/material/ListItemText";
import Divider from "@mui/material/Divider";
import { ListItemIcon } from "@mui/material";
import styles from "./SideBar.module.css";
import { Link, useLocation } from "react-router-dom";
import IconButton from "@mui/material/IconButton";
import OpenInFullIcon from "@mui/icons-material/OpenInFull";
import ListItems from "./side-bar-list";

interface propsTypes {
  open: boolean | undefined;
  handleDrawerToggle: () => void;
}

const SideBar: React.FC<propsTypes> = ({ open, handleDrawerToggle }) => {
  const { pathname } = useLocation();
  const isLocalEnvironment = process.env.NODE_ENV === "development";
  const basePath = isLocalEnvironment
    ? "/dashboard"
    : "/educational_ministry_irp";
  return (
    <Box component={"div"}>
      <Drawer anchor="left" open={open} onClose={handleDrawerToggle}>
        <IconButton
          aria-label="close open"
          onClick={() => handleDrawerToggle()}
          color="primary"
        >
          <OpenInFullIcon />
        </IconButton>
        <Divider />
        {ListItems.map((list, index) => {
          return (
            <ListItem
              key={index}
              component={Link}
              to={`${basePath}${list.to}`}
              disablePadding
            >
              <ListItemButton>
                <ListItemText
                  className={styles.listItemText}
                  primary={list.list}
                />
                <ListItemIcon style={{ justifyContent: "right" }}>
                  {list.icon}
                </ListItemIcon>
              </ListItemButton>
            </ListItem>
          );
        })}
      </Drawer>
    </Box>
  );
};

export default SideBar;
