import React, { FC, ReactNode, createContext, useReducer } from 'react'

import en from '../i18n/en.json';
import ko from '../i18n/ko.json'; 

enum LangActionType {
  SET_LANGUAGE = 'SET_LANGUAGE'
}

interface LangState {
  language: string;
}

interface LangStateProps {
  children: ReactNode;
}

interface SetLanguageAction {
  type: typeof LangActionType.SET_LANGUAGE;
  payload: string;
}

interface ContextProps {
  state: LangState;
  dispatch: {
    setLanguage: (lang: string) => void;
    translate: (key: string) => string;
  }
}

const langReducer = (state: LangState, action: SetLanguageAction): any => {
  switch(action.type) {
    case LangActionType.SET_LANGUAGE:
      return {
        language: action.payload
      }
    default:
      return state;
  }
}

const localStorageLang = localStorage.getItem('language');
const initialState = {
  language: localStorageLang ? localStorage : 'KO'
}

export const LangContext = createContext({} as ContextProps);

// eslint-disable-next-line @typescript-eslint/no-redeclare
const LangState: FC<LangStateProps> = ({ children }) => {
  const [state, dispatch] = useReducer(langReducer, initialState);

  const setLanguage = (lang: string) => {
    localStorage.setItem('language', lang);
    dispatch({
      type: LangActionType.SET_LANGUAGE,
      payload: lang
    });
  }

  function translate(key: string): string {
    const { language } = state;
    let langData: { [key: string]: string; } = {};

    if (language === 'KO') {
      langData = ko;
    } else if (language === 'EN') {
      langData = en;
    }

    return langData[key];
  }

  return(
    <LangContext.Provider value={{ state, dispatch: { setLanguage, translate } }}>
      {children}
    </LangContext.Provider>
  );
}

export default LangState;