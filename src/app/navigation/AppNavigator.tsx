import React from 'react';
import { Pressable } from 'react-native';
import {
  DarkTheme,
  DefaultTheme,
  LinkingOptions,
  NavigationContainer,
  Theme,
  useNavigation,
} from '@react-navigation/native';
import { createNativeStackNavigator, NativeStackNavigationProp } from '@react-navigation/native-stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import Icon from 'react-native-vector-icons/Ionicons';
import HomeScreen from '../../features/reading/screens/HomeScreen';
import BookScreen from '../../features/reading/screens/BookScreen';
import ReaderScreen from '../../features/reading/screens/ReaderScreen';
import QuizScreen from '../../features/reading/screens/QuizScreen';
import StatisticsScreen from '../../features/reading/screens/StatisticsScreen';
import SettingsScreen from '../../features/settings/screens/SettingsScreen';
import AboutScreen from '../../features/settings/screens/AboutScreen';
import { getBook, getText } from '../../features/reading/content';
import { SUITE_LINKS } from '../../core/config';
import { pick } from '../../i18n/l10n';
import { useSettings } from '../settings/SettingsContext';

export type RootStackParamList = {
  MainTabs: undefined;
  Book: { bookId: string };
  Reader: { textId: string };
  Quiz: { textId: string };
  Settings: undefined;
  About: undefined;
};
export type RootTabParamList = {
  Home: undefined;
  Statistics: undefined;
};
export type StackNav = NativeStackNavigationProp<RootStackParamList>;

const Stack = createNativeStackNavigator<RootStackParamList>();
const Tab = createBottomTabNavigator<RootTabParamList>();

const TAB_ICONS: Record<keyof RootTabParamList, [string, string]> = {
  Home: ['library', 'library-outline'],
  Statistics: ['stats-chart', 'stats-chart-outline'],
};

/** Derin bağlantı: linguauz-reading://text/<metin-id> → o metin açılır */
const linking: LinkingOptions<RootStackParamList> = {
  prefixes: [`${SUITE_LINKS.reading.scheme}://`],
  config: {
    initialRouteName: 'MainTabs',
    screens: {
      Reader: 'text/:textId',
      Book: 'book/:bookId',
    },
  },
};

function SettingsButton() {
  const nav = useNavigation<StackNav>();
  const { colors, t } = useSettings();
  return (
    <Pressable onPress={() => nav.navigate('Settings')} hitSlop={10} style={{ marginRight: 16 }} accessibilityLabel={t('screen.settings')}>
      <Icon name="settings-outline" size={22} color={colors.text} />
    </Pressable>
  );
}

function MainTabs() {
  const { colors, t } = useSettings();
  return (
    <Tab.Navigator
      screenOptions={({ route }) => ({
        tabBarActiveTintColor: colors.primary,
        tabBarInactiveTintColor: colors.textSecondary,
        headerRight: () => <SettingsButton />,
        tabBarIcon: ({ focused, color, size }) => {
          const [active, inactive] = TAB_ICONS[route.name];
          return <Icon name={focused ? active : inactive} size={size} color={color} />;
        },
      })}>
      <Tab.Screen name="Home" component={HomeScreen} options={{ title: t('tab.home') }} />
      <Tab.Screen name="Statistics" component={StatisticsScreen} options={{ title: t('tab.statistics') }} />
    </Tab.Navigator>
  );
}

export default function AppNavigator() {
  const { colors, isDark, t, language } = useSettings();
  const base = isDark ? DarkTheme : DefaultTheme;
  const navTheme: Theme = {
    ...base,
    colors: {
      ...base.colors,
      primary: colors.primary,
      background: colors.background,
      card: colors.surface,
      text: colors.text,
      border: colors.border,
    },
  };

  return (
    <NavigationContainer theme={navTheme} linking={linking}>
      <Stack.Navigator>
        <Stack.Screen name="MainTabs" component={MainTabs} options={{ headerShown: false }} />
        <Stack.Screen
          name="Book"
          component={BookScreen}
          options={({ route }) => ({ title: pick(getBook(route.params.bookId)?.title, language) })}
        />
        <Stack.Screen
          name="Reader"
          component={ReaderScreen}
          options={({ route }) => ({ title: `${t('reader.title')} · ${getText(route.params.textId)?.level ?? ''}` })}
        />
        <Stack.Screen name="Quiz" component={QuizScreen} options={{ title: t('quiz.title') }} />
        <Stack.Screen name="Settings" component={SettingsScreen} options={{ title: t('screen.settings') }} />
        <Stack.Screen name="About" component={AboutScreen} options={{ title: t('about.title') }} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
