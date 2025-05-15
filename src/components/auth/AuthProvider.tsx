"use client";
import type { ReactNode } from 'react';
import { AuthProviderClient } from '@/hooks/use-auth';

interface AuthProviderProps {
  children: ReactNode;
}

export function AuthProvider({ children }: AuthProviderProps) {
  return <AuthProviderClient>{children}</AuthProviderClient>;
}
