import React from "react";
import { userHasRole } from "../hooks/userHasRole";

export default function Authorized({ role, children }) {
  const allowed = userHasRole(role);
  return allowed ? <>{children}</> : null;
}