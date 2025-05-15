import Link from 'next/link';
import { Card, CardContent, CardDescription, CardHeader, CardTitle, CardFooter } from "@/components/ui/card";
import { LoginForm } from "@/components/auth/LoginForm";
import { Logo } from '@/components/layout/Logo';

export default function LoginPage() {
  return (
    <Card className="w-full max-w-md shadow-xl">
      <CardHeader className="space-y-1 text-center">
        <div className="mx-auto mb-4 flex justify-center">
           <Logo />
        </div>
        <CardTitle className="text-2xl">Welcome Back</CardTitle>
        <CardDescription>
          Enter your email and password to access your FinanceFlow account.
        </CardDescription>
      </CardHeader>
      <CardContent>
        <LoginForm />
      </CardContent>
      <CardFooter className="flex flex-col gap-2 text-center text-sm">
        <p>
          Don&apos;t have an account?{' '}
          <Link href="/signup" className="font-medium text-primary hover:underline">
            Sign up
          </Link>
        </p>
        {/* <Link href="/forgot-password" className="font-medium text-primary hover:underline">
            Forgot password?
        </Link> */}
      </CardFooter>
    </Card>
  );
}
