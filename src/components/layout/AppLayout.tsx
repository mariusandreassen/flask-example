"use client"

import type { ReactNode } from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import {
  LayoutDashboard,
  Users,
  Handshake, // For Customers
  Briefcase, // For Jobs
  PanelLeft,
  Settings,
} from 'lucide-react';
import {
  SidebarProvider,
  Sidebar,
  SidebarHeader,
  SidebarContent,
  SidebarFooter,
  SidebarMenu,
  SidebarMenuItem,
  SidebarMenuButton,
  SidebarTrigger,
  useSidebar,
} from '@/components/ui/sidebar';
import { Button } from '@/components/ui/button';
import { UserNav } from '@/components/auth/UserNav';
import { Logo } from '@/components/layout/Logo';
import { cn } from '@/lib/utils';

interface AppLayoutProps {
  children: ReactNode;
}

const navItems = [
  { href: '/dashboard', label: 'Dashboard', icon: LayoutDashboard },
  { href: '/employees', label: 'Employees', icon: Users },
  { href: '/customers', label: 'Customers', icon: Handshake },
  { href: '/jobs', label: 'Jobs', icon: Briefcase },
];

function LayoutContent({ children }: AppLayoutProps) {
  const pathname = usePathname();
  const { state: sidebarState } = useSidebar();
  const isCollapsed = sidebarState === "collapsed";

  return (
    <div className="flex h-screen bg-background">
      <Sidebar collapsible="icon" variant="sidebar">
        <SidebarHeader className="p-0 border-b border-sidebar-border">
          <div className={cn(
            "flex items-center justify-between h-16",
            isCollapsed ? "px-2" : "px-4"
          )}>
            <Logo collapsed={isCollapsed} />
          </div>
        </SidebarHeader>
        <SidebarContent className="flex-1 p-2">
          <SidebarMenu>
            {navItems.map((item) => (
              <SidebarMenuItem key={item.href}>
                <Link href={item.href} passHref legacyBehavior>
                  <SidebarMenuButton
                    isActive={pathname.startsWith(item.href)}
                    tooltip={{ children: item.label, className: "bg-popover text-popover-foreground" }}
                  >
                    <item.icon className="h-5 w-5" />
                    <span className={cn(isCollapsed && "hidden")}>{item.label}</span>
                  </SidebarMenuButton>
                </Link>
              </SidebarMenuItem>
            ))}
          </SidebarMenu>
        </SidebarContent>
        <SidebarFooter className="p-2 border-t border-sidebar-border">
           <SidebarMenu>
            <SidebarMenuItem>
                <SidebarMenuButton tooltip={{ children: "Settings", className: "bg-popover text-popover-foreground" }}>
                    <Settings className="h-5 w-5" />
                    <span className={cn(isCollapsed && "hidden")}>Settings</span>
                </SidebarMenuButton>
            </SidebarMenuItem>
           </SidebarMenu>
        </SidebarFooter>
      </Sidebar>

      <div className="flex flex-1 flex-col overflow-hidden">
        <header className="sticky top-0 z-10 flex h-16 items-center justify-between border-b bg-background/80 backdrop-blur-sm px-4 md:px-6">
          <SidebarTrigger className="md:hidden" />
          <div className="flex items-center gap-4 ml-auto">
            <UserNav />
          </div>
        </header>
        <main className="flex-1 overflow-y-auto p-4 md:p-6 lg:p-8">
          {children}
        </main>
      </div>
    </div>
  );
}


export function AppLayout({ children }: AppLayoutProps) {
  return (
    <SidebarProvider>
      <LayoutContent>{children}</LayoutContent>
    </SidebarProvider>
  );
}
