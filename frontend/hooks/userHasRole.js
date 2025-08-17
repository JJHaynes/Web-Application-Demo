import { useSession } from "next-auth/react";

export function userHasRole(required) {
  const { data: session, status } = useSession();

  if (status !== "authenticated" || !session?.user?.roles) {
    return false;
  }

  const rolesSet = new Set(session.user.roles);

  if (Array.isArray(required)) {
    return required.every(role => rolesSet.has(role));
  }

  return rolesSet.has(required);
}