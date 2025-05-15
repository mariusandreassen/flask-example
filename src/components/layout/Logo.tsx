import Link from 'next/link';
import { Briefcase } from 'lucide-react'; // Using Briefcase as a generic business icon

export function Logo({ collapsed } : { collapsed?: boolean }) {
  return (
    <Link href="/dashboard" className="flex items-center gap-2 px-2 h-12 text-sidebar-foreground hover:text-sidebar-primary-foreground transition-colors duration-200">
      <Briefcase className="h-7 w-7 text-sidebar-primary" />
      {!collapsed && <span className="text-xl font-semibold">FinanceFlow</span>}
    </Link>
  );
}
