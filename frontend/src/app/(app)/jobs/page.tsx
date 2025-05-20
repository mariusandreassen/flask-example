import { Button } from "../../../components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "../../../components/ui/card";
import { PlusCircle, Filter, Search } from "lucide-react";
import { Input } from "../../../components/ui/input";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "../../../components/ui/table";
import { Badge } from "../../../components/ui/badge";

export default function JobsPage() {
  const jobs = [
    { id: "JOB001", title: "Website Redesign", customer: "Globex Corporation", status: "In Progress", deadline: "2024-08-15" },
    { id: "JOB002", title: "Mobile App Development", customer: "Stark Industries", status: "Open", deadline: "2024-09-01" },
    { id: "JOB003", title: "Marketing Campaign", customer: "Wayne Enterprises", status: "Completed", deadline: "2024-07-20" },
  ];

  return (
    <div className="space-y-6">
      <div className="flex flex-col md:flex-row items-center justify-between gap-4">
        <h1 className="text-3xl font-bold tracking-tight">Jobs</h1>
        <div className="flex items-center gap-2 w-full md:w-auto">
          <div className="relative flex-1 md:flex-initial">
            <Search className="absolute left-2.5 top-2.5 h-4 w-4 text-muted-foreground" />
            <Input type="search" placeholder="Search jobs..." className="pl-8 w-full md:w-[300px]" />
          </div>
          <Button variant="outline">
            <Filter className="mr-2 h-4 w-4" /> Filter
          </Button>
          <Button>
            <PlusCircle className="mr-2 h-5 w-5" /> Create Job
          </Button>
        </div>
      </div>
      
      <Card>
        <CardHeader>
          <CardTitle>Job List</CardTitle>
          <CardDescription>Manage all ongoing and past jobs.</CardDescription>
        </CardHeader>
        <CardContent>
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>ID</TableHead>
                <TableHead>Title</TableHead>
                <TableHead>Customer</TableHead>
                <TableHead>Status</TableHead>
                <TableHead>Deadline</TableHead>
                <TableHead>Actions</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {jobs.map((job) => (
                <TableRow key={job.id}>
                  <TableCell className="font-medium">{job.id}</TableCell>
                  <TableCell>{job.title}</TableCell>
                  <TableCell>{job.customer}</TableCell>
                  <TableCell>
                    <Badge variant={
                      job.status === "Completed" ? "secondary" : job.status === "In Progress" ? "default" : "outline"
                    } className={
                      job.status === "In Progress" ? "bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-200 border-blue-300" : 
                      job.status === "Open" ? "bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-200 border-yellow-300" :
                      "bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200 border-green-300" // Completed
                    }>
                      {job.status}
                    </Badge>
                  </TableCell>
                  <TableCell>{job.deadline}</TableCell>
                  <TableCell>
                    <Button variant="outline" size="sm">Details</Button>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </CardContent>
      </Card>
    </div>
  );
}
