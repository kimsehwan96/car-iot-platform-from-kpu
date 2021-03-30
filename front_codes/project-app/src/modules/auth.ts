import  UserInfo  from '../interfaces/user';

const users: UserInfo[] = [
  { email: 'kwhong95@kakao.com', password: '123123', username: "홍경원"  },
];

export function logIn({ email, password, username }: UserInfo) {
  const user = users.find(
    (user) => user.email === email && user.password === password
  )
  if (user === undefined) throw new Error(`not found ${username}`)
  return user;
}