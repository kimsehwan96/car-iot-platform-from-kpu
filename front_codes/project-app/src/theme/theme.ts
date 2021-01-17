import { createMuiTheme } from "@material-ui/core";
import { blue } from "@material-ui/core/colors";

export const darkTheme = createMuiTheme({
  palette: {
    type: 'dark',
    primary: {
      main: '#202020',
    },
  },
});

export const lightTheme = createMuiTheme({
  palette: {
    type: 'light',
    primary: blue
  }
})